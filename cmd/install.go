package cmd

import (
	"os"
	"os/exec"

	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

func DownloadBPaks(args []string, repos map[string]map[string]string) bool {
	cats := repos["bpak"]
	color.Blue("Looking for Git...")
	var ret = false
	if _, err := exec.LookPath("git"); err == nil {
		color.Green("Git found!")
		ret = loadCache(cats)
	} else {
		return false
	}
	return ret
}

func loadCache(cats map[string]string) bool {
	color.Blue("Looking for cache...")
	if err := os.Mkdir(getTemporaryPath()+"core", os.ModePerm); err == nil {
		color.Red("Cache not found")
		color.Blue("Loading cache...")
		for k, v := range cats {
			cmd := exec.Command("git", "clone", v, getTemporaryPath()+k)
			cobra.CheckErr(cmd.Run())
		}
		color.Green("Successiful")
		return false
	}
	color.Green("Found the cache")
	return true
}

// installCmd represents the install command
var installCmd = &cobra.Command{
	Use:   "install",
	Short: "install a package",
	Long:  ``,
	Args:  cobra.MinimumNArgs(1),
	Run: func(cmnd *cobra.Command, args []string) {
		cats := repos["bpak"]
		color.Blue("Looking for Git...")
		if _, err := exec.LookPath("git"); err == nil {
			color.Green("Git found!")
			loadCache(cats)
		}
	},
}

func init() {
	rootCmd.AddCommand(installCmd)
}
